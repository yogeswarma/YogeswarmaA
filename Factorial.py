def fact_recv(n):

  if n == 0 or n == 1:
    return 1
  else:

    return n * fact_recv(n - 1)


number = int(input("enter the value to factorial :"))

res = fact_recv(number)

print("the factorial 0f number{} is {}.".format(number, res))
