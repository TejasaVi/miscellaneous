#include <stdio.h>
#include <string.h>
#include <uuid/uuid.h>

#include "qbuffer.h"
#include "shared_mem_allocator.h"

q_buf *create_buffer_q(int max_num) {
	q_buf *tmp, *head;
	char *cur;
        uuid_t uuid;
        char uuid_str[37];
	
	//allocate shared buffer for the struct;
	head = (q_buf*) s_mem_alloc(NULL, sizeof(q_buf));
	cur = head->name;
        uuid_generate_time_safe(uuid);
        uuid_unparse_lower(uuid, uuid_str);
	strncpy(head->sbuf_nxt, uuid_str, 37);

	for(int i=1; i<max_num;i++) {
		tmp = s_mem_alloc(uuid_str, sizeof(q_buf));
		uuid_generate_time_safe(uuid);
	        uuid_unparse_lower(uuid, uuid_str);
        	strncpy(tmp->sbuf_nxt, uuid_str, 37);

	}
	strncpy(tmp->sbuf_nxt,'\0',1);
	return head;
}

void print_q(q_buf *head) {
	q_buf *tmp;
	printf("[%s] ", head->name);

	while(strncmp(tmp->name,'\0',1) || tmp->name != head->name) {
		printf("[%s] ", tmp->name);
	}
	printf("\n");

}
int make_circular(q_buf *head, char *hname) {
	q_buf *tmp = head;
	while(tmp->sbuf_nxt != NULL) {
		tmp = tmp->sbuf_nxt;
	}
	
	if(hname == NULL){
		strncpy(tmp->sbuf_nxt, "head",4);
	}
	else {
		strncpy(tmp->sbuf_nxt, hname, strlen(hname));
	}
	return 0;
}

int atomic_write_buffer(q_buf *node, char *string){return 0;}
int atomic_read_buffer(q_buf *node, char *string){return 0;}

int main()
{
	q_buf *head = create_buffer_q(3);
	print_q(head);
	return 0;
}
