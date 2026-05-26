# 代码文件头部注释模板

每个代码文件开头包含三行注释，格式如下：

## TypeScript / JavaScript

```typescript
// input:  [依赖外部的什么（参数、导入的模块）]
// output: [对外提供什么（导出的是什么）]
// pos:    [在系统局部中的地位/职责]
// ⚠️ 一旦此文件被更新，务必更新头部注释及所属文件夹的 FOLDER.md
```

## Python

```python
# input:  [依赖外部的什么（参数、导入的模块）]
# output: [对外提供什么（导出的类/函数）]
# pos:    [在系统局部中的地位/职责]
# ⚠️ 一旦此文件被更新，务必更新头部注释及所属文件夹的 FOLDER.md
```

## Go

```go
// input:  [依赖外部的什么（参数、导入的包）]
// output: [对外提供什么（导出的函数/结构体）]
// pos:    [在系统局部中的地位/职责]
// ⚠️ 一旦此文件被更新，务必更新头部注释及所属文件夹的 FOLDER.md
```

## Java / C++ / C#

```java
// input:  [依赖外部的什么（参数、导入的类）]
// output: [对外提供什么（公开的方法/类）]
// pos:    [在系统局部中的地位/职责]
// ⚠️ 一旦此文件被更新，务必更新头部注释及所属文件夹的 FOLDER.md
```

---

## 示例

### Good Example (TypeScript)

```typescript
// input:  UserService (用户服务), UserRepository (数据库操作)
// output: UserController (处理用户相关 HTTP 请求)
// pos:    用户模块的 HTTP 入口，负责请求解析和响应格式化
// ⚠️ 一旦此文件被更新，务必更新头部注释及所属文件夹的 FOLDER.md

import { UserService } from './user.service';
import { UserRepository } from './user.repository';

export class UserController {
  // ...
}
```

### Bad Example

```typescript
// 用户控制器
// 负责处理用户相关请求
// update: 2024-01-01
```

❌ 没有遵循 input/output/pos 格式，无法快速了解模块依赖和职责。
