Verify cpp sections are formatted correctly
.
```cpp
int main  (int  argc , char const ** argv) 
{
return 0 ;
}
```
.
```cpp
int main(int argc, char const** argv) {
  return 0;
}
```
.
Verify cxx sections are formatted correctly
.
```cxx
int main  (int  argc , char const ** argv) 
{
return 0 ;
}
```
.
```cxx
int main(int argc, char const** argv) {
  return 0;
}
```
.
Verify c++ sections are formatted correctly
.
```c++
int main  (int  argc , char const ** argv) 
{
return 0 ;
}
```
.
```c++
int main(int argc, char const** argv) {
  return 0;
}
```
.
Verify c sections are formatted correctly
.
```c
int main  (int  argc , char const ** argv) 
{
return 0 ;
}
```
.
```c
int main(int argc, char const** argv) {
  return 0;
}
```
.
Verify objective c sections are formatted correctly
.
```obj-c
int main  (int  argc , char const ** argv) 
{
return [ obj getCount] ;
}
```
.
```obj-c
int main(int argc, char const** argv) {
  return [obj getCount];
}
```
.
Verify objective c sections are formatted correctly
.
```objective-c
int main  (int  argc , char const ** argv) 
{
  return [ obj getCount] ;
}
```
.
```objective-c
int main(int argc, char const** argv) {
  return [obj getCount];
}
```
.
Verify objc sections are formatted correctly
.
```objc
int main  (int  argc , char const ** argv) 
{
return [ obj getCount] ;
}
```
.
```objc
int main(int argc, char const** argv) {
  return [obj getCount];
}
```
.
Verify objectivec sections are formatted correctly
.
```objectivec
int main  (int  argc , char const ** argv) 
{
  return [ obj getCount] ;
}
```
.
```objectivec
int main(int argc, char const** argv) {
  return [obj getCount];
}
```
.
Verify obj-c++ sections are formatted correctly
.
```obj-c++
int main  (int  argc , char const ** argv) 
{
return [ obj getCount] ;
}
```
.
```obj-c++
int main(int argc, char const** argv) {
  return [obj getCount];
}
```
.
Verify objective-c++ sections are formatted correctly
.
```objective-c++
int main  (int  argc , char const ** argv) 
{
  return [ obj getCount] ;
}
```
.
```objective-c++
int main(int argc, char const** argv) {
  return [obj getCount];
}
```
.
Verify objc++ sections are formatted correctly
.
```objc++
int main  (int  argc , char const ** argv) 
{
return [ obj getCount] ;
}
```
.
```objc++
int main(int argc, char const** argv) {
  return [obj getCount];
}
```
.
Verify objectivec++ sections are formatted correctly
.
```objectivec++
int main  (int  argc , char const ** argv) 
{
  return [ obj getCount] ;
}
```
.
```objectivec++
int main(int argc, char const** argv) {
  return [obj getCount];
}
```
.
Verify csharp sections are formatted correctly
.
```csharp
class TestClass
{
    static void Main(string[] args)
    {
        Console.WriteLine(args.Length);
    }
}
```
.
```csharp
class TestClass {
  static void Main(string[] args) { Console.WriteLine(args.Length); }
}
```
.
Verify c# sections are formatted correctly
.
```c#
class TestClass
{
    static void Main(string[] args)
    {
        Console.WriteLine(args.Length);
    }
}
```
.
```c#
class TestClass {
  static void Main(string[] args) { Console.WriteLine(args.Length); }
}
```
.
Verify cs sections are formatted correctly
.
```cs
class TestClass
{
    static void Main(string[] args)
    {
        Console.WriteLine(args.Length);
    }
}
```
.
```cs
class TestClass {
  static void Main(string[] args) { Console.WriteLine(args.Length); }
}
```
.
Verify java sections are formatted correctly
.
```java
public class Test {

	public static void main(String[] args){

		System.out.println("Hello, World!");
	
	}
}
```
.
```java
public class Test {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```
.
Verify javascript sections are formatted correctly
.
```javascript
function foo(p1, p2)
{
    // a comment
}
```
.
```javascript
function foo(p1, p2) {
  // a comment
}
```
.
Verify typescript sections are formatted correctly
.
```typescript
function foo(p1, p2) : number
{
    // a comment
    return 1.0;
}
```
.
```typescript
function foo(p1, p2): number {
  // a comment
  return 1.0;
}
```
.
Verify ts sections are formatted correctly
.
```ts
function foo(p1, p2) : number
{
    // a comment
    return 1.0;
}
```
.
```ts
function foo(p1, p2): number {
  // a comment
  return 1.0;
}
```
.
Verify json sections are formatted correctly
.
```json
"glossary": 
{
    "title": "example glossary",
    "GlossDiv": 
    {
        "title": "S"
    }
}
```
.
```json
"glossary": {
  "title": "example glossary",
           "GlossDiv": {
    "title": "S"
  }
}
```
.
Verify json-object sections are formatted correctly
.
```json-object
"glossary": 
{
    "title": "example glossary",
    "GlossDiv": 
    {
        "title": "S"
    }
}
```
.
```json-object
"glossary": {
  "title": "example glossary",
           "GlossDiv": {
    "title": "S"
  }
}
```
.
Verify protobuf sections are formatted correctly
.
```protobuf
syntax = "proto3";

message SearchRequest 
{
         string query = 1;
int32 page_number = 2;
 int32 results_per_page = 3;
}
```
.
```protobuf
syntax = "proto3";

message SearchRequest {
  string query = 1;
  int32 page_number = 2;
  int32 results_per_page = 3;
}
```
.
Verify proto sections are formatted correctly
.
```proto
syntax = "proto3";

message SearchRequest 
{
         string query = 1;
int32 page_number = 2;
 int32 results_per_page = 3;
}
```
.
```proto
syntax = "proto3";

message SearchRequest {
  string query = 1;
  int32 page_number = 2;
  int32 results_per_page = 3;
}
```
.
Verify tablegen sections are formatted correctly
.
```tablegen
class FPFormat<bits<3> val>
{
     bits<3> Value = val;
}

def NotFP :    FPFormat<0> ;
def ZeroArgFP  : FPFormat<1>;
def    OneArgFP : FPFormat<2>;
```
.
```tablegen
class FPFormat<bits<3> val> {
  bits<3> Value = val;
}

def NotFP : FPFormat<0>;
def ZeroArgFP : FPFormat<1>;
def OneArgFP : FPFormat<2>;
```
.
Verify td sections are formatted correctly
.
```td
class FPFormat<bits<3> val>
{
     bits<3> Value = val;
}

def NotFP :    FPFormat<0> ;
def ZeroArgFP  : FPFormat<1>;
def    OneArgFP : FPFormat<2>;
```
.
```td
class FPFormat<bits<3> val> {
  bits<3> Value = val;
}

def NotFP : FPFormat<0>;
def ZeroArgFP : FPFormat<1>;
def OneArgFP : FPFormat<2>;
```
.
Verify verilog sections are formatted correctly
.
```verilog
module and_gate (
input a,
  input    b,
    output o
);

```
.
```verilog
module and_gate
    (input a,
     input b,
     output o);
```
.
Verify v sections are formatted correctly
.
```v
module and_gate (
input a,
  input    b,
    output o
);

```
.
```v
module and_gate
    (input a,
     input b,
     output o);
```
.
Verify unmarked sections aren't called.
.
```
int main  (int  argc , char const ** argv) 
{
return 0 ;
}
```
.
```
int main  (int  argc , char const ** argv) 
{
return 0 ;
}
```
.
Verify sections we don't support remain unformatted
.
```cvv
int main  (int  argc , char const ** argv) 
{
return 0 ;
}
```
.
```cvv
int main  (int  argc , char const ** argv) 
{
return 0 ;
}
```