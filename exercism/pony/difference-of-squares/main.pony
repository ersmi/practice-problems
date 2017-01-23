use "collections" // Range

class Squares
  fun sum_of_squares(i : USize) : USize =>
    if i == 1 then
      i
    else
      (i * i) + this.sum_of_squares(i-1)
    end

  fun square_of_sums(i : USize) : USize =>
    var a : USize = i
    for n in Range(0,i) do
      a = n + a
    end
    a * a

  fun difference(i : USize) : USize =>
    this.square_of_sums(i) - this.sum_of_squares(i)
