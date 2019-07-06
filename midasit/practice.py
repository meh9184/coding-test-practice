arr = [2,4,7,2,5]


# input / output
intput = gets.chomp()
puts intput


# if
if arr.length % 2 == 1
  puts '홀수 개'
elsif arr.length % 2 == 0
  puts '짝수 개'
else
  puts '있을 수 없는 경우'
end


# for
for i in 0...5
  puts "#{i}번째 값 = #{arr[i]}"
end


# while
i=0
while i < arr.length
  puts "#{i}번째 값 = #{arr[i]}"
  i += 1
end


# each
arr.each do |a|
  puts "#{a}"
end


# map
arr2 = arr.map {|a|
  a + 1
}
puts arr2


# inject
grades = [88,99,73,56,87,64] 
sum = grades.inject do |stock, grade|
  stock + grade
end
average = sum / grades.length
puts average


# include
str = 'eunhwan moon'
puts str.include? 'moon'


# 대문자 변환
str = 'eunhwan moon'
for i in 0...str.length
  str[i] = str[i].upcase
end
puts str


# int <-> string
str = '123'
int = 123
puts str.to_i + 123
puts int.to_s + '123'