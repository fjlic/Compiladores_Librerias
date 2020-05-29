program matrix
implicit none

!Matriz A de dimensión 3x3 donde se guardarán los valores del archivo txt, la matriz B contendrá la matriz resultante
!integer, dimension(3,3) :: A, B
real, dimension(3,3) :: A, B

integer :: row,col,max_rows,max_cols

row = 1;
col = 1;
max_rows = 3;
max_cols = 3;

open(10, file="parameters.txt")

read(10,*)((A(row,col),col=1,max_cols),row=1,max_rows)
B=matmul(A,A)

print*,("La matriz original es:")
do row=1, max_rows
  print*,(A(row,col),col=1,max_cols)
end do

print*,("La matriz multiplicada por si misma es:")
do row=1, max_rows
  print*,(B(row,col),col=1,max_cols)
end do

close(10)

end program matrix

