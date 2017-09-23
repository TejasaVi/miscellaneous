#include "shared_mem_allocator.h"
#include <uuid/uuid.h>

int main()
{
        uuid_t uuid;
        uuid_generate_time_safe(uuid);
        char uuid_str[37];
        uuid_unparse_lower(uuid, uuid_str);

        s_mem_alloc(NULL, 1);
        s_mem_alloc(uuid_str, 1);
        return 0;
}

