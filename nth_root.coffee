nthRootMe = (m, n) ->
  z = undefined
  power = (aa, bb) ->
    cc = 1
    i = 0
    while i < bb
      cc *= aa
      i++
    cc

  repe = (x) ->
    a = m / power(x, n - 1)
    b = (a + x * (n - 1)) / n
    if x == (x + b) / 2
      z = parseFloat(x.toString(10))
    else
      repe (x + b) / 2
    return

  repe 1
  console.log z
  return

#to find 10th root of 1024
nthRootMe 1024, 10
