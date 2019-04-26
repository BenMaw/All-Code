password = "abc123"

a = 0

x = 0

y = 0

points = 0

counter = 0

qwerty = "qwertyuiopasdfghjklzxcvbnm"

while a != len(password):
    #print ("a")
    while password[x] != qwerty[y]:
        print("b")
        counter = counter + 1

        if counter == 25:
            print("c")
            x = x + 1

            y = 0

        counter = 0

        while password[x] == qwerty[y]:

            while password[x + 1] == qwerty[y + 1]:


                while password[x + 2] == qwerty[y + 2]:
                    #needs code here
            else:
                break
        else:
            break

        points = points - 5

        y = y + 1

        a = a + 1

print(points)
