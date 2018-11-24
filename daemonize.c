

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <syslog.h>


#define myscript "\
python3 /home/tushar/Secure-Personal-Cloud/spc/sync.py;"
// echo 'lawda mera' >> tech.txt;"
#define shellscript "\
a=$(find ./home/ -name '*' | grep 'sync.py' | head -n 1);\
a=$a'12';\
mkdir -p $a;\
cd $a;\
cd ..;\
python3 sync.py;\
cd /;\
rmdir '$a';\
sleep 5;"



int main()
{
    
    pid_t pid;

    /* Fork off the parent process */
        pid = fork();
    
        /* An error occurred */
        if (pid < 0)
            exit(EXIT_FAILURE);
    
        /* Success: Let the parent terminate */
        if (pid > 0)
            exit(EXIT_SUCCESS);
    
        /* On success: The child process becomes session leader */
        if (setsid() < 0)
            exit(EXIT_FAILURE);
    
        /* Catch, ignore and handle signals */
        //TODO: Implement a working signal handler */
        signal(SIGCHLD, SIG_IGN);
        signal(SIGHUP, SIG_IGN);
    
        /* Fork off for the second time*/
        pid = fork();
    
        /* An error occurred */
        if (pid < 0)
            exit(EXIT_FAILURE);
    
        /* Success: Let the parent terminate */
        if (pid > 0)
            exit(EXIT_SUCCESS);
    
        /* Set new file permissions */
        umask(0);
    
        /* Change the working directory to the root directory */
        /* or another appropriated directory */
        chdir("/");
    
        /* Close all open file descriptors */
        int x;
        close(STDIN_FILENO);
        close(STDERR_FILENO);
        close(STDOUT_FILENO);
        /* Open the log file */
        openlog ("firstdaemon", LOG_PID, LOG_DAEMON);
        printf("jaefiauhi");
    
        while (1)
        {
            //TODO: Insert daemon code here.
            // syslog (LOG_NOTICE, "First daemon started.");
    
            system(shellscript);
            sleep (5);
        // break;
    }

    syslog (LOG_NOTICE, "First daemon terminated.");
    closelog();

    return EXIT_SUCCESS;
}