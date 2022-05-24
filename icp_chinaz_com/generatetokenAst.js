/* ==================================
# @Time    : 2022-05-18
# @Author  : 微信公众号：K哥爬虫
# @FileName: generatetokenAst.js
# @Software: PyCharm
# ================================== */


const fs = require("fs");
const parse = require("@babel/parser").parse;
const generate = require("@babel/generator").default
const traverse = require("@babel/traverse").default
const types = require("@babel/types")

// 导入混淆代码并解析为 AST
const oldCode = fs.readFileSync("generatetoken.js", {encoding: "utf-8"});
const astCode = parse(oldCode);

// 获取整个 AST 节点的长度
let astCodeLength = astCode.program.body.length

// 获取解密函数的名字 也就是 _0x530e
let decryptFunctionName = astCode.program.body[3].id.name

// 分割加密函数和解密函数，即 body 的前四部分和后面剩余部分
let decryptFunction = astCode.program.body.slice(0, 4)
let encryptFunction = astCode.program.body.slice(4, astCodeLength)

// 获取加密函数和解密函数的方法多种多样，比如可以挨个取值并转换成 JS 代码
// 这样做就不需要将解密函数赋值给整个 AST 节点了
// let decryptFunction = "";
// for(let i=0; i<4; i++){
//     decryptFunction += generate(astCode.program.body[i], {compact: true}).code
// }
// eval(decryptFunction);

// 将解密函数赋值给整个 AST 节点
astCode.program.body = decryptFunction

// 将 AST 节点转换成 JS 代码，并 eval 执行一下
decryptFunction = generate(astCode, {compact: true}).code
eval(decryptFunction);

// 测试一下，直接调用 _0x530e 函数可以正确拿到结果
// 输出 split
// console.log(_0x530e('‮b', 'Zp9G'))

// 将加密函数赋值给整个 AST 节点，此时整个节点就没有大数组、自执行函数和解密函数了
astCode.program.body = encryptFunction

// 调用解密函数，直接计算出类似以下方法的值并替换
// 混淆代码：_0x530e('‮b', 'Zp9G')
// 还原后：split
const visitor1 = {
    CallExpression(path){
        if (path.node.callee.name === decryptFunctionName && path.node.arguments.length === 2){
            path.replaceInline(types.stringLiteral(eval(path.toString())))
        }
    }
}

let functionName = {
    "_0x3b79c6": {},
    "_0x278b2d": {},
    "_0x4115c4": {},
    "_0xd8ec33": {}
}

// 单独提取出四个大对象
const visitor2 = {
    VariableDeclarator(path){
        for (let key in functionName){
            if (path.node && path.node.id.name == key) {
                const properties = path.node.init.properties
                for (let i=0; i<properties.length; i++){
                    functionName[key][properties[i].key.value] = properties[i].value
                }
                // 写入对象后就可以删除该节点了
                path.remove()
            }
        }
    }
}

// 函数替换，字符串替换：将类似 _0x3b79c6['YrYQW'] 变成 '#IpValue'
const visitor3 = {
    MemberExpression(path) {
        for (let key in functionName){
            if (path.node.object && path.node.object.name == key && path.inList ) {
                path.replaceInline(functionName[key][path.node.property.value])
            }
            if (path.node.object && path.node.object.name == key && path.parent.property && path.parent.property.value == "split") {
                path.replaceInline(functionName[key][path.node.property.value])
            }
        }
    }
}

// 函数替换，二项式计算：将类似 _0x278b2d['CnTaO'](_0x691267["length"], 0x1) 变成 _0x691267["length"] - 0x1
// 函数替换，方法调用：将类似 _0x4115c4["PJbSm"](getRandom, 0x64, 0x3e7) 变成 getRandom(0x64, 0x3e7)
const visitor4 = {
    CallExpression(path){
        for (let key in functionName) {
            if (path.node.callee && path.node.callee.object && path.node.callee.object.name == key) {
                let func = functionName[key][path.node.callee.property.value]
                if (func.body.body[0].argument.type == "BinaryExpression") {
                    let operator = func.body.body[0].argument.operator
                    let left = path.node.arguments[0]
                    let right = path.node.arguments[1]
                    path.replaceInline(types.binaryExpression(operator, left, right))
                }
                if (func.body.body[0].argument.type == "CallExpression") {
                    let identifier = path.node.arguments[0]
                    let arguments = path.node.arguments.slice(1)
                    path.replaceInline(types.callExpression(identifier, arguments))
                }
            }
        }
    }
}

// switch-case 反控制流平坦化
const visitor5 = {
    WhileStatement(path) {
        // switch 节点
        let switchNode = path.node.body.body[0];
        // switch 语句内的控制流数组名，本例中是 _0x28073a、_0x2efb35、_0x187fb8
        let arrayName = switchNode.discriminant.object.name;
        // 获取控制流数组绑定的节点
        let bindingArray = path.scope.getBinding(arrayName);
        // 获取节点整个表达式的参数、分割方法、分隔符
        let init = bindingArray.path.node.init;
        let object = init.callee.object.value;
        let property = init.callee.property.value;
        let argument = init.arguments[0].value;
        // 模拟执行 '3|2|1|4|5|0|6'['split']('|') 语句
        let array = object[property](argument)
        // 也可以直接取参数进行分割，方法不通用，比如分隔符换成 , 就不行了
        // let array = init.callee.object.value.split('|');

        // switch 语句内的控制流自增变量名，本例中是 _0x38c69e、_0x396880、_0x3b3dc7
        let autoIncrementName = switchNode.discriminant.property.argument.name;
        // 获取控制流自增变量名绑定的节点
        let bindingAutoIncrement = path.scope.getBinding(autoIncrementName);
        // 可选择的操作：删除控制流数组绑定的节点、自增变量名绑定的节点
        bindingArray.path.remove();
        bindingAutoIncrement.path.remove();

        // 储存正确顺序的控制流语句
        let replace = [];
        // 遍历控制流数组，按正确顺序取 case 内容
        array.forEach(index => {
                let consequent = switchNode.cases[index].consequent;
                // 如果最后一个节点是 continue 语句，则删除 ContinueStatement 节点
                if (types.isContinueStatement(consequent[consequent.length - 1])) {
                    consequent.pop();
                }
                // concat 方法拼接多个数组，即正确顺序的 case 内容
                replace = replace.concat(consequent);
            }
        );
        // 替换整个 while 节点，两种方法都可以
        path.replaceWithMultiple(replace);
        // path.replaceInline(replace);
    }
}

const visitor6 = {
    // 十六进制、Unicode 编码等，转正常字符
    "StringLiteral|NumericLiteral"(path){
        delete path.node.extra;
    },
    // _0x3cbc20["length"] 转换成 _0x3cbc20.length
    MemberExpression(path){
        if (path.node.property.type == "StringLiteral") {
            path.node.computed = false
            path.node.property = types.identifier(path.node.property.value)
        }
    },
    // 表达式还原，!![] 直接计算成 true
    "BinaryExpression|UnaryExpression"(path) {
        const {confident, value} = path.evaluate()
        if (confident){
            path.replaceInline(types.valueToNode(value))
        }
    },
    // 删除未引用的变量，比如 _0xodD = "jsjiami.com.v6";
    AssignmentExpression(path){
        const binding = path.scope.getBinding(path.node.left.name);
        if (!binding) {
            path.remove();
        }
    }
}

// 删除冗余逻辑代码，只保留 if 为 true 的
const visitor7 = {
    IfStatement(path) {
        if(path.node.test.type == "BooleanLiteral") {
            if(path.node.test.value) {
                path.replaceInline(path.node.consequent.body)
            } else {
                path.replaceInline(path.node.alternate.body)
            }
        }
    }
}

// 遍历节点
traverse(astCode, visitor1)
traverse(astCode, visitor2)
traverse(astCode, visitor3)
traverse(astCode, visitor4)
traverse(astCode, visitor5)
traverse(astCode, visitor6)
traverse(astCode, visitor7)

// 将 AST 节点转换成 JS 代码并写入到新文件里
const result = generate(astCode, {concise:true}).code
fs.writeFile("./generatetokenNew.js", result, (err => {console.log(err)}))
