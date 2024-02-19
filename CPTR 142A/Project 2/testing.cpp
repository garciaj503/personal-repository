#include <iostream>
#include <cassert>
#include "headers.h"

int main() {

	std::cout << "Testing started." << std::endl;
	//Testing function OtherDoorFrom
	assert(OtherDoorFrom(1, 1) == 2);
	assert(OtherDoorFrom(1, 2) == 3);
	assert(OtherDoorFrom(1, 3) == 2);
	assert(OtherDoorFrom(2, 1) == 3);
	assert(OtherDoorFrom(2, 2) == 1);
	assert(OtherDoorFrom(2, 3) == 1);
	assert(OtherDoorFrom(3, 1) == 2);
	assert(OtherDoorFrom(3, 2) == 1);
	assert(OtherDoorFrom(3, 3) == 1);

	//Testing function SwitchDoorTo
	assert(SwitchDoorTo(1, 1) == 3);
	assert(SwitchDoorTo(1, 2) == 2);
	// assert(SwitchDoorTo(1, 3) == 2);
	// assert(SwitchDoorTo(2, 1) == 3);
	// assert(SwitchDoorTo(2, 2) == 3);
	// assert(SwitchDoorTo(2, 3) == 1);
	// assert(SwitchDoorTo(3, 1) == 2);
	// assert(SwitchDoorTo(3, 2) == 1);
	// assert(SwitchDoorTo(3, 3) == 2);

	std::cout << "..." << std::endl;
	std::cout << "Testing finished. 0 errors" << std::endl;

  return 0;
}
