##initialize
my_chr=ARG[1]
my_file=ARG[2]
chr={
   'chr1':[0,3000000],
   'chr2':[0,3250000],
   'chr3':[0,3000000]...      
}
## Initialize
bed=[]
for (i=chr[my_file][0];i<=chr[my_file][1];++i) {
    bed[i]=0;    
}


## processfile

for lineInFile {
    (chr,start, end,cov)=split(lineInFile,tab)   
   for (i=start;i<end;i=i+50) {
      if (i % 50 != 0) {die "unexpected iteration}
      bed[i]=cov
    
    }
    
}
## print
for (i=chr[my_file][0];i<=chr[my_file][1];i=i+50) {
    print(my_chr,i,i+50,bed[i])
}
