#include <iostream>
#include <functional>

void Print(const std::string& HE) 
{
	std::cout << HE << "\n";
}

template<typename Sig>
class FunctionC
{
public:
	bool CALL;

	FunctionC(Sig&& Function)
		: Function(std::forward<Sig>(Function)), CALL(false)
	{
		CALL = std::_Test_callable(this->Function);
	}

	template<typename ... PARAMS>
	decltype(auto) operator()(PARAMS& ... Args)
	{
		return std::invoke(Function, Args...);
	}

private:
	Sig Function;
};

int main()
{
	FunctionC<decltype(&Print)> FunctionC(&Print);

	FunctionC("HELLO PENIS MY OLD FREIND, COVERD BY YOUD DARKNESS ONCE AGAIn");

	return 0;
}