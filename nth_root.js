function nthRootMe(m,n)
{
	var z;

	//Replacement for Math.pow
	function power(aa,bb){
		var cc=1;
		for(i=0;i<bb;i++){
			cc*=aa
		}
		return cc
	}
  function repe(x)
  {
    var a,b;
    a=m/power(x,n-1);
    b=(a+(x*(n-1)))/n;
    if(x==(x+b)/2)
    {
      z=parseFloat(x.toString(10))
    }
    else
    {
      repe((x+b)/2);
    }
  }
  repe(1);
  console.log(z)
}
//Function called here
//m=999 and n=3
//cube root of 999 is calculated here.
nthRootMe(999,3)
