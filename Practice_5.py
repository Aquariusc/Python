height=input('请输入您的身高(米)：')
weight=input('请输入您的体重(千克)：')
height=float(height)
weight=float(weight)
bmi=weight/(height*height)
if 0<bmi<18.5:
	print('您的BMI指数为：%.2f , 过轻！'%bmi)
elif 18.5<=bmi<25:
	print('您的BMI指数为：%.2f ，正常！'%bmi)
elif 25<=bmi<28:
	print('您的BMI指数为：%.2f ，过重！'%bmi)
elif 28<=bmi<32:
	print('您的BMI指数为：%.2f ，肥胖！'%bmi)
else :
	print('您的BMI指数为：%.2f ，严重肥胖！'%bmi)