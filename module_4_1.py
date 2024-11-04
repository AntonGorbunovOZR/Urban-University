import fake_math  as div1
import true_math  as div2

fake_divide = div1.divide
true_divide = div2.divide

result1 = fake_divide(69, 3)

result2 = fake_divide(3, 0)

result3 = true_divide(49, 7)

result4 = true_divide(15, 0)

print(result1)

print(result2)

print(result3)

print(result4)
