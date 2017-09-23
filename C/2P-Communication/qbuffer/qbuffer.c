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
	for(int i=1; i<max_num;i++) {
		
        	uuid_generate_time_safe(uuid);
        	uuid_unparse_lower(uuid, uuid_str);
		tmp = s_mem_alloc(uuid_str, sizeof(q_buf));
		if(i==1) { 
			strncpy(head->sbuf_nxt, uuid_str, 37);
		}
		else{
			strncpy(cur, uuid_str, 37);
		}
	}
	return 0;
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
	return 0;
}
