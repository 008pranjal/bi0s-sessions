BITS 32

extern printf
extern scanf

section .data 
    int: db "%d",0
    correct: db "Prime Number",10,0
    incorrect: db "Not Prime Number",10,0

section .text

    global main

    main:
    push ebp
    mov ebp,esp

    lea eax, [ebp-0x4]
	push eax
	push int
	call scanf
    
    
    mov eax,[ebp-0x4] 
    mov ecx,2  
    cmp eax,1
    je false
    mov edx,0
    L1:
        cmp ecx,[ebp-0x4]
        je true   
        div ecx
        cmp edx,0
        je false
        mov edx,0
        mov eax,[ebp-0x4]
        inc ecx
        jmp L1
        

    true:
        push correct
        call printf
        leave
        ret

    false:
        push incorrect
        call printf
        leave
        ret
