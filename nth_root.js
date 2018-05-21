function squareRootMe(n,c)
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
    a=n/power(x,c-1);
    b=(a+(x*(c-1)))/c;
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
