a=1
b={}
function luafunc() 
  local count = 1
  return function (  )
    count = count + 1
    return count
  end
end
if a<=1 then
  print(a)
end
if a<1 then
  print(a)
elseif b.a then
  print(b)
  -- body
end
a="this string is used for testing lua"
b=string.gsub( a,"lua","python" )
print(b)
