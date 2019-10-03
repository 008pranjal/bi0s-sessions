BITS 32


extern printf
extern scanf



section .rodata
        int: db "%d",0
        

section .text

	global main
	

        main:
      
        push ebp
        mov ebp,esp
      
       

        lea ebx,[ebp-0x4]
                push ebx 
                push int
                call scanf

	mov ebx,[ebp-0x4]	
        mov eax, ebx
        
   	
	L1:
        sub ebx,0x1
        cmp ebx,0x1
	jle ext

	mul ebx
	jmp L1
	
 
        ext:
        push eax
	call printf
        leave
        ret
