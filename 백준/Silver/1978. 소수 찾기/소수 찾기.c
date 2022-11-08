#include<stdio.h>
int main() {
	int n;
	int count = 0,cnt=0;
	scanf("%d", &n);
	int arr[100];
	for (int i = 0; i < n;i++)
		scanf("%d",&arr[i]);

	for (int j = 0; j < n;j++) {
		for (int k = 1;k <= arr[j];k++) {
			if (arr[j] % k == 0)
				count++;
		}
		if (count == 2) {
			cnt = cnt + 1;
		}
			count = 0;
				
	}
	printf("%d", cnt);
}
	

