# intermod
A service that allows for the 
* Open
* Reliable
* Performant
* Extensible
* Secure

distribution of software artifacts.

### Challenges
#### File integrity
How do we ensure that a file arrives in the same state as it left in? The obvious answer is to obtain a checksum at source, embed the checksum as metadata then validate upon extraction.

Of course the problem becomes what do we do if the checksum mismatches at the destination ?