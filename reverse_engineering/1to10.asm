BITS 32

extern printf

section .rodata
	int: db "%d",10,0

section .text 

	global main
	
	main:
	push ebp
	mov ebp, esp

	mov ebx,0
	L1:
	inc  ebx
	push ebx
	push int
	call printf
	cmp ebx,10
	jl L1
	
	leave
	ret
