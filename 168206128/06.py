 #include<stdio.h>
  void main()
  {
  	int a,b,c,d;
  	for(a=1;a>=0;a--)
  		for(b=1;b>=0;b--)
  			for(c=1;c>=0;c--)
  				for(d=1;d>=0;d--)
  					if((a==0)+(b==1)+(d==1)+(d==0)==3&&a+b+c+d==1)
  					{
  						if(a==0)
  							printf("A没有偷钻石\n");
  						else
  							printf("A偷了钻石\n");
  						if(b==0)
  							printf("B没有偷钻石\n");
  						else
  							printf("B偷了钻石\n");
  						if(c==0)
  							printf("C没有偷钻石\n");
  						else
  							printf("C偷了钻石\n");
  						if(d==0)
  							printf("D没有偷钻石\n");
  						else
  							printf("D偷了钻石\n");
  					}
