import os
from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout, CMakeToolchain
from conan.tools.files import copy

class UnoDBRecipe(ConanFile):
    name = "unodb"
    version = "0.1.0"
    license = "Apache Public License 2.0"
    author = "Laurynas Biveinis"
    url = "https://github.com/vidyasilai/unodb"
    description = "Adaptive Radix Tree Implementation Library"
    topics = ("data structures",)

    tool_requires = [
        "cmake/[>=3.20.0]",
    ]

    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "*.cpp", "*.hpp", "CMakeLists.txt"

    def requirements(self):
        self.requires("boost/[>=1.84.0]")
    
    def layout(self):
        cmake_layout(self)

    def configure(self):
        self.options["boost"].shared = False
        self.options["boost"].without_test = True
    
    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables['TESTS'] = False
        tc.variables['STATS'] = False
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "*.hpp", dst=os.path.join(self.package_folder, "include"), src=self.source_folder)
        copy(self, "*.a", dst=os.path.join(self.package_folder, "lib"), src=self.build_folder, keep_path=False)
        copy(self, "*.so", dst=os.path.join(self.package_folder, "lib"), src=self.build_folder, keep_path=False)
        copy(self, "*.dll", dst=os.path.join(self.package_folder, "bin"), src=self.build_folder, keep_path=False)
        copy(self, "*.dylib", dst=os.path.join(self.package_folder, "lib"), src=self.build_folder, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["unodb"]
