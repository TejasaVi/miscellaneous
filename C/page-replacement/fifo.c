#include<stdio.h>


int main(){
	int no_frames, no_pg;
	int i, j,k, free_slots, no_hits, no_fault, first_in;
	int hit_flag;
	printf("Enter No on frames:");
	scanf("%d",&no_frames);
	int frames[no_frames];
	for(i=0;i<no_frames;i++)
		frames[i] = -1;

	printf("Enter no of Page refernces:");
	scanf("%d",&no_pg);
	int pages[no_pg];
	for(i=0;i<no_pg;i++)
		scanf("%d",&pages[i]);

	free_slots = no_frames;
	no_fault = 0;
	no_hits = 0;
	first_in = 0;
	for(i=0;i<no_pg;i++){
		hit_flag = 0;

		if((free_slots-1) >= 0){
			for(k = 0;k<no_frames;k++){
				if(frames[k] == pages[i]){
					no_hits += 1;
					hit_flag = 1;
					break;
				}
			}
			if(!hit_flag){
				frames[no_frames - free_slots] = pages[i];
				free_slots = free_slots - 1;
				no_fault += 1;
			}
		}
		else{

			for(k = 0;k<no_frames;k++){
				if(frames[k] == pages[i]){
					no_hits += 1;
					hit_flag = 1;
					break;
				}
			}

			if(!hit_flag){
				frames[first_in] = pages[i];
				no_fault += 1;
				first_in = ((first_in + 1 )% no_frames);

			}
		}
		printf("Frames at the end of [%d]\n",pages[i]);
		for(j = 0;j<no_frames;j++)
			printf("%d\t",frames[j]);
		printf("\n");
	}
    printf("no_fault: [%d] no_hits: [%d]\n",no_fault, no_hits);

	return 0;
}
