from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import copy
import os

include_path = os.path.abspath("./include")

# example command: 
# conan build . -s build_type=Debug -s compiler.runtime=static -s arch=x86 --build=missing

class ZeroTierConanFile(ConanFile):
    name = "libzt"
    version = "1.8.10"
    build_requires = "cmake/3.29.3"
    requires = "nlohmann_json/3.11.3"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        info = self.dependencies["nlohmann_json"].cpp_info
        copy(self, "*.h", info.includedirs[0], include_path)
        copy(self, "*.hpp", info.includedirs[0], include_path)

    def build(self):
        cmake = CMake(self)
        cmake.configure(variables={"BUILD_HOST_SELFTEST":False})
        cmake.build()
