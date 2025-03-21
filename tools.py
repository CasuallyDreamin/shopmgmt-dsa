from random import randint
def generate_ship_id(type):
    return f"{chr(randint(65,90))}\
{chr(randint(65,90))}\
{chr(randint(65,90))}\
{(randint(0,9))}\
{(randint(0,9))}\
{(randint(0,9))}\
{(randint(0,9))}\
{(randint(0,9))}\
{(randint(0,9))}\
{(randint(0,9))}\
{(randint(0,9))}\
{type}"

print(generate_ship_id('D'))