# this program calculate the fee for the next 5 years
# having yearly percent increase

# NUMBER_YEAR = 5
# CURRENT_SEMESTER_FEE = 8000
# yearly_fee = CURRENT_SEMESTER_FEE * 2
# NUMBER_SEMESTER = 2 * NUMBER_YEAR
#PERCENT_INCREASE_PER_YEAR = 0.03    # THIS IS BASICALLY 3 PERCENT INCREASE
# total_fee = 0.0
# fee = 8000

next_fee  = 0
na_fee = 0
print('year\t tution fee')
for x in range(1,11) :
    fee = 8000
    next_fee += fee + fee*0.015
    fee += fee * 0.015
    print(x, '\t\t ', next_fee/)



     # +=next_fee

#print("the fee for total semesters having increase yearly also : ")


def main():
    tuition = 8000
    print('Num.Years\Tuition$')
    print('------------------')
    print()
    for years in [1, 2, 3, 4, 5,6,7,8,9,10]:
        tuition += (1.5 / 100) * tuition
        print(years, '\t', format(tuition, '.2f'))


main()











