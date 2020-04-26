#include<stdio.h>

typedef struct{
	int data;
	int time;
}page_t;


int FindLRU(page_t page_list[], int len){
	int min =page_list[0].time;
	int it, pos=0;
	for(it=1;it<len;it++){
		if(page_list[it].time < min){
			pos = it;
		}
	}
	return pos;
}



int main(){
	int i,j, flag;
	int no_frames, no_pg, free_slots;
	int no_pg_fault=0, no_pg_hit = 0;
	int counter = 0;
    printf("Enter No on frames:");
    scanf("%d",&no_frames);
    page_t frames[no_frames];
    for(i=0;i<no_frames;i++){
        frames[i].data = -1;
		frames[i].time = 999;
	}

    printf("Enter no of Page refernces:");
    scanf("%d",&no_pg);
    page_t pages[no_pg];
    for(i=0;i<no_pg;i++)
        scanf("%d",&pages[i].data);

	free_slots = no_frames;
	for(i=0;i<no_pg;i++){
		flag =0;
		 if((free_slots-1) >= 0){
			// Page hit (page being refernced is already present in page frame)
			for(j=0;j<no_frames;j++){
				if(frames[j].data == pages[i].data){
					flag = 1;
					no_pg_hit +=1;
					frames[j].time = counter++;
					break;
				}
			}
			// Page Fault (page being refernced is a new page)
            if(!flag){
                frames[no_frames - free_slots].data = pages[i].data;
				frames[no_frames - free_slots].time = counter++;
                free_slots = free_slots - 1;
                no_pg_fault += 1;
            }

		}else{
			for(j=0;j<no_frames;j++){
				if(frames[j].data == pages[i].data){
					no_pg_hit +=1;
					frames[j].time = counter++;
					flag = 1;
					break;
				}
			}
			// Page Fault (page being refernced is not present in frames)
			if(!flag){
				frames[FindLRU(pages, no_pg)].data = pages[i].data;
				no_pg_fault+=1;
			}
		}
        printf("Frames at the end of [%d]\n",pages[i]);
        for(j = 0;j<no_frames;j++)
            printf("%d\t",frames[j].data);
        printf("\n");
	}

	printf("no_pg_hit= %d no_pg_fault= %d\n",no_pg_hit,no_pg_fault);
	return 0;
}
