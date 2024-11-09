from math import comb
# Данные задачи
total_balls_box1 = 10
white_balls_box1 = 7
total_balls_box2 = 11
white_balls_box2 = 9
# Вероятности извлечения двух белых мячей из первого ящика
prob_two_white_box1 = comb(white_balls_box1, 2) /comb(total_balls_box1, 2)
# Вероятности извлечения двух белых мячей из второго ящика
prob_two_white_box2 = comb(white_balls_box2, 2) /comb(total_balls_box2, 2)
# Вероятность, что все мячи белые
prob_all_white = prob_two_white_box1 * prob_two_white_box2
print(f"Вероятность того, что все мячи белые: {prob_all_white:.5f}")
# Вероятность того, что ровно два мяча белые
prob_one_white_box1 = (comb(white_balls_box1, 1) *
comb(total_balls_box1 - white_balls_box1, 1)) /comb(total_balls_box1, 2)
prob_one_white_box2 = (comb(white_balls_box2, 1) *
comb(total_balls_box2 - white_balls_box2, 1)) /comb(total_balls_box2, 2)
prob_two_white_exactly = (prob_two_white_box1 * prob_one_white_box2)
+ (prob_one_white_box1 * prob_two_white_box2)
print(f"Вероятность того, что ровно два мяча белые:{prob_two_white_exactly:.5f}")
# Вероятность того, что хотя бы один мяч белый
prob_no_white_box1 = comb(total_balls_box1 - white_balls_box1, 2) /comb(total_balls_box1, 2)
prob_no_white_box2 = comb(total_balls_box2 - white_balls_box2, 2) /comb(total_balls_box2, 2)
prob_at_least_one_white = 1 - (prob_no_white_box1 *prob_no_white_box2)
print(f"Вероятность того, что хотя бы один мяч белый:{prob_at_least_one_white:.5f}")