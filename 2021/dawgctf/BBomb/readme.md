# Binary Bomb
## phase 3
### decompile
#### phase3()
```c++
bool phase3(undefined8 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4,
           undefined4 param_5,undefined4 param_6,undefined4 param_7,undefined4 param_8,char *param_9
           )
{
  int iVar1;
  char *flag;
  char *current1;
  undefined8 in_R8;
  undefined8 in_R9;
  undefined4 extraout_XMM0_Da;
  undefined in_stack_ffffffffffffffc8;
  char *current;
  
  puts("\nReflections? Rotations? Translations? This is starting to sound like geometry...");
  flag = (char *)calloc(0x29,1);
  getInput(extraout_XMM0_Da,param_2,param_3,param_4,param_5,param_6,param_7,param_8,3,param_9,
           &DAT_001028d1,flag,in_R8,in_R9,in_stack_ffffffffffffffc8);
  current = flag;
  while (*current != '\0') {
    current1 = func3_1(current);
    *current = *current1;
    current1 = func3_2(current);
    *current = *current1;
    current = current + 1;
  }
  iVar1 = strcmp(flag,"\"_9~Jb0!=A`G!06qfc8\'_20uf6`2%7");
  free(flag);
  return iVar1 == 0;
}
```

#### func3_1()
```c++
char * func3_1(char *char)
{
  char cVar1;
  
  if (('@' < *char) && (*char < '[')) {
    *char = *char + -0xd;
    if (*char < 'A') {
      cVar1 = '\x1a';
    }
    else {
      cVar1 = '\0';
    }
    *char = cVar1 + *char;
  }
  if (('`' < *char) && (*char < '{')) {
    *char = *char + -0xd;
    if (*char < 'a') {
      cVar1 = '\x1a';
    }
    else {
      cVar1 = '\0';
    }
    *char = cVar1 + *char;
  }
  return char;
}
```
#### func3_2()
```c++
char * func3_2(char *char)

{
  char cVar1;
  
  if ((' ' < *char) && (*char != '\x7f')) {
    *char = *char + -0x2f;
    if (*char < '!') {
      cVar1 = '^';
    }
    else {
      cVar1 = '\0';
    }
    *char = cVar1 + *char;
  }
  return char;
}
```

## phase 4
### decompile
#### phase4()
```c++
undefined4
phase4(undefined8 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4,
      undefined4 param_5,undefined4 param_6,undefined4 param_7,undefined4 param_8,char *param_9)

{
  long lVar1;
  long lVar2;
  void *__ptr;
  long lVar3;
  long in_FS_OFFSET;
  undefined4 extraout_XMM0_Da;
  undefined4 success;
  int index;
  long list1 [5];
  long local_20;
  
  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  puts("\nThis is the phase you have been waiting for... one may say it\'s the golden stage!");
  puts(
      "Let\'s switch things up! Numerical inputs map to line numbers in rockyou.txt, and each wordis separated by a \'_\' (if the phase\'s solution is 4 5, the flag would beDawgCTF{password_iloveyou})"
      );
  success = 1;
  list1[0] = 1;
  list1[1] = 0x7b;
  list1[2] = 0x3b18;
  list1[3] = 0x1c640d;
  lVar2 = func4(10);
  __ptr = calloc(4,4);
  getInput(extraout_XMM0_Da,param_2,param_3,param_4,param_5,param_6,param_7,param_8,4,param_9,
           "%d%d%d%d",__ptr,(long)__ptr + 4,(long)__ptr + 8,(char)__ptr + '\f');
  index = 0;
  while (index < 4) {
    lVar1 = list1[index];
    lVar3 = func4(*(int *)((long)__ptr + (long)index * 4));
    if (lVar1 * (int)lVar2 - lVar3 != 0) {
      success = 0;
    }
    index = index + 1;
  }
  free(__ptr);
  if (local_20 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return success;
}
```

#### func4()
```c++

long func4(int param_1)

{
  long lVar1;
  long lVar2;
  
  if (param_1 < 1) {
    lVar1 = 0;
  }
  else {
    if (param_1 == 1) {
      lVar1 = 1;
    }
    else {
      lVar2 = func4(param_1 + -1);
      lVar1 = func4(param_1 + -2);
      lVar1 = lVar1 + lVar2;
    }
  }
  return lVar1;
}
```