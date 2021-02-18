# duplCertDetect
Detecting duplicate certs before enabling ssl in glusterfs

For those who have been using glusterfs for sometime now, enabling and using SSL starts with the process of certificate creation.
Now this can be either a self signed certificate, i.e. you create your own certs for the nodes and combine the certs to create
a glusterfs.ca ( basically appending all the public certs of nodes into a file ), or derive your certs from a root CA following
the process of certificate signing etc, etc.

This python script is basically concerned about the method 1, wherein we create self signed certificates. Due to human error 
or an issue with the algorithm being used to concatenate the certs into a .ca file ( which again is technically human error only
as it was a human who wrote the code ), there might be a duplicate entry of a certificate or two.

This duplicate entry would lead to some grave issues when one goes ahead and enables the ssl in glusterfs and one might look into
an error of the form -> [2021-02-18 11:11:11.12312] E [socket.c:246:ssl_dump_error_stack] 0-socket.management:   error:0B07C065:x509 certificate routines:X509_STORE_add_cert:cert already in hash table

Which actually implies a duplicate entry inside the glusterfs.ca.

This script is about taking a pre-emptive approach and checking the glusterfs.ca for any existing duplicates inside them. ( I'd suggets using ansible
to run this script in all nodes and get the result to check if everything is well and good before enabling the ssl option ).

To run the script one just needs to give the path to the glusterfs.ca
`python3 dupl_cert.py <path_to_glusterfs.ca>`

If there are any duplicate entries, the script will dump those public keys.
