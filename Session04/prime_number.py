def tell_if_a_number_prime_number():

    numb = int(input("Enter a number: "))
    is_prime = True
    i = 2 
    while i < numb:
        if numb % i == 0:
            is_prime = False

        i+= 1
        if i == numb:
            loop = False

    if is_prime:
        print("{} is a prime number".format(numb))
    else:
        print("{} is not a prime number".format(numb))


tell_if_a_number_prime_number()