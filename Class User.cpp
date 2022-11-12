#include <iostream>
#include <string>
#include <vector>


class User
{

private:
std::string login;
std::string password;
std::vector<std::string> data;

public:
User(std::string login, std::string password="Qwerty123") //login -логин не меньше 4 символов. Пароль не короче 8 символов
{
    this->login=login;
    this->password=password;
    
}

};

