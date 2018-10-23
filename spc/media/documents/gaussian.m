n=10;

ans=zeros(1,5000);

for i=[1:5000]

ans(i)=((sum(rand(1,n))/n)-0.5)*(n^0.5);

end

histogram(ans);
