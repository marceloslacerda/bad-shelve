# bad-shelve
A project that was created to observe the bad behavior of shelve during upgrades of the python interpreter

Using docker and this project it's possible to test various versions of shelve and observe their different behaviors.

## Observed behaviours:

* On Python 3.4.2 passing a file name without .db to the shelve.open function caused a file with the .db extension to be created. This no longer happens in newer versions.
* Databases created with shelve >=3.4.5 cannot be read by shelve 3.4.2 and vice versa.



## Example

Creating a database file with Python 3.4.5 and reading it with 3.5.2:

docker run -it -v "/path-to-bad-shelve:/root/shelve" python:3.4  bash -c "python /root/shelve/test-write.py"
docker run -it -v "/path-to-bad-shelve:/root/shelve" python:3.5  bash -c "python /root/shelve/test-read.py /root/shelve/file3.4.5"
