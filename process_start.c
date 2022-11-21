#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

static char child_stack[1048576];

static int start()
{
    printf("PID: %ld\n", (long)getpid());
    FILE *fp = NULL;
    fp = fopen("test2.txt","a");
    fprintf(fp,"Wololoo");
    fclose(fp);
    system("sh benchmark.sh | tee container_benchmark_results.txt");
    return 0;
}

int main()
{
    pid_t child_pid = clone(start, child_stack+1048576,
                            CLONE_NEWPID | CLONE_NEWNET | CLONE_NEWNS | SIGCHLD, NULL);

    waitpid(child_pid, NULL, 0);
    return 0;
}
