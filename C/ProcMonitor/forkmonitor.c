#define  _POSIX_C_SOURCE 200809L
#include <unistd.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <signal.h>
#include <pwd.h>
#include <grp.h>
#include <string.h>
#include <stdio.h>
#include <errno.h>
#include "forkmonitor.h"

static volatile sig_atomic_t  done = 0;

static void done_handler(const int signum)
{
    if (!done)
        done = signum;
}

static int catch_done(const int signum)
{
    struct sigaction  act;

    sigemptyset(&act.sa_mask);
    act.sa_handler = done_handler;
    act.sa_flags = 0;

    if (sigaction(signum, &act, NULL) == -1)
        return errno;

    return 0;
}

static const char *username(const uid_t uid)
{
    static char    buffer[128];
    struct passwd *pw;

    pw = getpwuid(uid);
    if (!pw)
        return NULL;

    strncpy(buffer, pw->pw_name, sizeof buffer - 1);
    buffer[sizeof buffer - 1] = '\0';

    return (const char *)buffer;
}

static const char *groupname(const gid_t gid)
{
    static char   buffer[128];
    struct group *gr;

    gr = getgrgid(gid);
    if (!gr)
        return NULL;

    strncpy(buffer, gr->gr_name, sizeof buffer - 1);
    buffer[sizeof buffer - 1] = '\0';

    return (const char *)buffer;
}

int main(int argc, char *argv[])
{
    const size_t    msglen = 65536;
    struct message *msg;
    int             socketfd, result;
    const char     *user, *group;

    if (catch_done(SIGINT) || catch_done(SIGQUIT) || catch_done(SIGHUP) ||
        catch_done(SIGTERM) || catch_done(SIGPIPE)) {
        fprintf(stderr, "Cannot set signal handlers: %s.\n", strerror(errno));
        return 1;
    }

    if (argc != 2 || !strcmp(argv[1], "-h") || !strcmp(argv[1], "--help")) {
        fprintf(stderr, "\n");
        fprintf(stderr, "Usage: %s [ -h | --help ]\n", argv[0]);
        fprintf(stderr, "       %s MONITOR-SOCKET-PATH\n", argv[0]);
        fprintf(stderr, "\n");
        fprintf(stderr, "This program outputs events reported by libforkmonitor\n");
        fprintf(stderr, "to Unix domain datagram sockets at MONITOR-SOCKET-PATH.\n");
        fprintf(stderr, "\n");
        return 0;
    }

    msg = malloc(msglen);
    if (!msg) {
        fprintf(stderr, "Out of memory.\n");
        return 1;
    }

    socketfd = socket(AF_UNIX, SOCK_DGRAM, 0);
    if (socketfd == -1) {
        fprintf(stderr, "Cannot create an Unix domain datagram socket: %s.\n", strerror(errno));
        return 1;
    }

    {
        struct sockaddr_un  addr;
        size_t              len;

        if (argv[1])
            len = strlen(argv[1]);
        else
            len = 0;
        if (len < 1 || len >= UNIX_PATH_MAX) {
            fprintf(stderr, "%s: Path is too long (max. %d characters)\n", argv[1], UNIX_PATH_MAX - 1);
            return 1;
        }

        memset(&addr, 0, sizeof addr);
        addr.sun_family = AF_UNIX;
        memcpy(addr.sun_path, argv[1], len + 1); /* Include '\0' at end */

        if (bind(socketfd, (struct sockaddr *)&addr, sizeof (addr)) == -1) {
            fprintf(stderr, "Cannot bind to %s: %s.\n", argv[1], strerror(errno));
            return 1;
        }
    }

    printf("Waiting for connections.\n");
    printf("\n");

    /* Infinite loop. */
    while (!done) {
        ssize_t  n;

        n = recv(socketfd, msg, msglen, 0);
        if (n == -1) {
            const char *const errmsg = strerror(errno);
            fprintf(stderr, "%s.\n", errmsg);
            fflush(stderr);
            break;
        }

        if (msglen < sizeof (struct message)) {
            fprintf(stderr, "Received a partial message; discarded.\n");
            fflush(stderr);
            continue;
        }

        switch (msg->type) {
        case TYPE_EXEC:
            printf("Received an EXEC message:\n");
            break;
        case TYPE_DONE:
            printf("Received a DONE message:\n");
            break;
        case TYPE_FORK:
            printf("Received a FORK message:\n");
            break;
        case TYPE_VFORK:
            printf("Received a VFORK message:\n");
            break;
        case TYPE_EXIT:
            printf("Received an EXIT message:\n");
            break;
        case TYPE_ABORT:
            printf("Received an ABORT message:\n");
            break;
        default:
            printf("Received an UNKNOWN message:\n");
            break;
        }

        if (msg->type == TYPE_EXEC && (size_t)n > sizeof (struct message)) {
            if (*((char *)msg + n - 1) == '\0')
                printf("\tExecutable:        '%s'\n", (char *)msg + sizeof (struct message));
        }

        printf("\tProcess ID:         %d\n", (int)msg->pid);
        printf("\tParent process ID:  %d\n", (int)msg->ppid);
        printf("\tSession ID:         %d\n", (int)msg->sid);
        printf("\tProcess group ID:   %d\n", (int)msg->pgid);

        user = username(msg->uid);
        if (user)
            printf("\tReal user:         '%s' (%d)\n", user, (int)msg->uid);
        else
            printf("\tReal user:          %d\n", (int)msg->uid);

        group = groupname(msg->gid);
        if (group)
            printf("\tReal group:        '%s' (%d)\n", group, (int)msg->gid);
        else
            printf("\tReal group:         %d\n", (int)msg->gid);

        user = username(msg->euid);
        if (user)
            printf("\tEffective user:    '%s' (%d)\n", user, (int)msg->euid);
        else
            printf("\tEffective user:     %d\n", (int)msg->euid);

        group = groupname(msg->egid);
        if (group)
            printf("\tEffective group:   '%s' (%d)\n", group, (int)msg->egid);
        else
            printf("\tEffective group:    %d\n", (int)msg->egid);

        printf("\n");
        fflush(stdout);
    }

    do {
        result = close(socketfd);
    } while (result == -1 && errno == EINTR);

    unlink(argv[1]);

    return 0;
}
