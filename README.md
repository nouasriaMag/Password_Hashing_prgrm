# Password_Hashing_prgrm
Repo on the usage of Argon2id and whatnot.

so what we're going to do is to install bcrypt via the venv.
`python -m venv .venv`
`source .venv/bin/activate`
`pip install bcrypt`

This program is a password hashing progran.
Password hashing turns a password into a fixed-length scrambled string using a one-way function, so the real password is never stored. At login you hash what the user typed and compare it to the stored hash.