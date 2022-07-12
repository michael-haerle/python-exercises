# You have rented some movies for your kids: 
# The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?
lm = 3
bb = 5
h = 1
movie_total = (lm + bb + h) * 3
print(movie_total, "dollars")
# Suppose you're working as a contractor for 3 companies: 
# Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
google = (400 * 6)
amazon = (380 * 4)
facebook = (350 * 10)
total_pay = (google + amazon + facebook)
print("Total Pay = $", total_pay)
# A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

class_not_full = True
no_schedule_conflict = False
can_enroll = class_not_full and no_schedule_conflict

# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

pre_mem = True
more_then_2_items = False
not_expired = True

not_expired and (more_then_2_items or pre_mem)

# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

pass_more_then_four = (len(password) > 4)
user_less_then_21 = len(username) <= 20
user_pass = username != password
no_whitespace = username == username.strip()
passed = no_whitespace and user_pass and\
user_less_then_21 and pass_more_then_four

username = 'codeup'
# if len(username) <= 20 False
# else true
password = 'notastrongpassword'
# if len(password) < 5 False
# else true
# username != password