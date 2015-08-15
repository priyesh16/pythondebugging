#!/usr/sbin/dtrace -ZCs

#pragma D option quiet

python$target:::function-entry
/ strstr(copyinstr(arg0) , "introspect") != NULL / 
{
	self->ts = vtimestamp;
}

python$target:::function-return
/ strstr(copyinstr(arg0) , "introspect") != NULL / 
{
   @totaltime[copyinstr(arg1)] = sum((vtimestamp - self->ts));
   @totalcount[copyinstr(arg1)] = count();
   self->ts = 0;
}

python$target:::function-entry
/
strstr(copyinstr(arg0) , "introspect") != NULL && 
strstr(copyinstr(arg1) , "importmodule") != NULL 
/ 
{
   jstack();
}
END
{
   printf("%-30s %-30s %-30s \n", "FUNCTION NAME", "TOTAL TIME", "TOTAL COUNT");
   printa("  %-30s %@-30d %@-30d \n", @totaltime, @totalcount);
}
