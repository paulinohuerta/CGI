#!/usr/bin/perl -w
#
#PROGRAM: Create form CGI Program
#
#Purpose: Desmostrate (1) how to create a form complete in CGI doing
# 		so my first program CGI.	
#
#	Create by Jesus Sigler.
#

#-------------------------------------------#
#  1. Create a new Perl CGI object and Redis #
#-------------------------------------------#

use CGI;
use Redis;
$query = new CGI;
$redis = new Redis;
$log=0;
my @Hobbies = fhobbies();

#----------------------------------#
#  2. Print the doctype statement  #
#----------------------------------#

print $query->header(-charset => 'utf8');

#----------------------------------------------------#
#  3. Start the HTML doc, and give the page a title  #
#----------------------------------------------------#

print $query->start_html('My first form CGI');

#------------------------------------------------------------#
#  4.  If the the password is equal at the password Redis, print   #
#       My first form CGI, else invalid password.                             #
#------------------------------------------------------------#
if ($query->param('the_password')) {
            $yourPassword = $query->param('the_password');
            if($yourPassword eq $redis->get("pass")) {
               $log=1;
            }
            else {
              print $query->h3('password incorrecta');
            
            }
}if($log){
	print $query->start_form;
	print $query->h3('Personal data');
	print $query->label('Nombre: ');
	print $query->textfield(-name=>'nombre',
			-size=>25,
			-maxlength=>50);
	print $query->br;
	print $query->br;
	print $query->label('Apellidos: ');
	print $query->textfield(-name=>'apellidos',
			-size =>25,
			-maxlength=>50);
	print $query->br;
	print $query->br;
	print $query->label('Email: ');
	print $query->textfield(-name=>'email',
			-size =>25,
			-maxlength=>60);
	print $query->br;
	print $query->br;
	print $query->label('Password: ');
	print $query->password_field(-name=>'yourPassword',
                -size=>9,
                -maxlength=>50);
	print $query->h3('Indica tu edad');
	print $query->radio_group(
        -name     => 'Checkbox',
        -values   => ['<10', '> 10 <= 18', '18', '>18'],
        -columns  => 2,
        -rows     => 2,
    );
    print $query->br;
    print $query->br;
    print $query->h4('Escribe aqui tu opinion sobre el formulario');
    print $query->textarea(
        -name  => 'textarea',
        -value => 'Write here...',
        -cols  => 60,
        -rows  => 3,);

    print $query->br;

	print $query->h3('Select your favorite hobby(ies): ');
	print $query->scrolling_list(-name=>'hobbies',
		-values=>\@Hobbies,
				 -size=>8,
				 -multiple=>'true');
	# Notes:
	# ------
	#	"-multiple=>'true'" lets the user make multiple selections
	#		from the scrolling_list
	#	"-default" is optional
	#	"-size" lets you specify the number of visible rows in the list
	#	can also use an optional "-labels" parameter to let the user
	#		see labels you want them to see, while you use
	#		different names for each parameter in your program
	
	print $query->br;
	print $query->br;
	print $query->submit(-value=>'Submit your Formulary');
	print $query->end_form;
}
#-------------------------------------------------------------#
# 5. if the program have params, print favorite(s) hobbies #
#-------------------------------------------------------------#
if($query->param('hobbies')){
	print $query->h3('your favorites hobbies are:');
	@Hobbies = $query->param('hobbies');
	print "<BLOCKQUOTE>\n";
	foreach $hobbies (@Hobbies) {
		print "$hobbies<br>";
	}
	print "</BLOCKQUOTE>\n";
}

#------------------------------------------------#
#6. if the program is called whithout any params, print password_field #
#------------------------------------------------#
if (!$query->param) {
            print $query->start_form;
            print $query->password_field(-name=>'the_password',
                -size=>35,
                -maxlength=>50);
            print $query->br;
            print $query->submit(-value=>'Submit tu password');
            print $query->end_form;
}
print $query->end_html;

sub fhobbies() {
 my @Hobbies;
 open F, '/tmp/Hobbies.txt' or die "No se puede abrir:$!";
 while(<F>){
  chomp;
  push (@Hobbies, $_);
 }
 close F;
 return @Hobbies;
}
