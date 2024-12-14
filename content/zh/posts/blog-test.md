---
title: "Hugo搭建个人博客"
date: 2024-12-07T12:11:08+08:00
draft: false
lastmod: 2024-12-07T12:11:08+08:00
tags: ["Blog", "hugo"]
categories: ["tools"]
authors:
  - "ryluiiwan"
---

之前尝试过很多次自己搭建个人博客，总是无疾而终，没有耐性、三心二意应该是我最大的缺点。最近裸辞休养生息还是觉得要做点什么，还是来完成我 22 年还是 23 年就想做的事情，创建一个个人博客。很多事情对我来说，我很难坚持从头到尾做完，没有强烈的热情，总是想一出是一出。

这次也想看看我能不能把这件事，从头到尾做完，并不断完善。准备开始折腾，顺便捡起本科的渣渣编程基础。有天在搜索 Hugo 的时候突然看到了[pseudoyu](https://www.pseudoyu.com/zh/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)大佬做的博客，故按照他的教程来搞一个静态的博客，做一个自己的网络自留地。

# 1. 安装 Hugo

我的电脑是 `windows` 系统，比 Mac os 安装起来麻烦一点点。
Windows 系统下载安装

## (1)下载 Hugo

- 打开 [Hugo 官方 GitHub Release 页面](https://github.com/gohugoio/hugo/releases)。
- 找到最新版本，下载适合 Windows 的二进制文件：
  - 如果你的 Windows 是 64 位，选择 `hugo_extended_x.y.z_Windows-64bit.zip`（`x.y.z` 是版本号）
  - 如果不需要扩展功能（如 SCSS 支持），也可以选择普通的 `hugo_x.y.z_Windows-64bit.zip`

## (2)解压文件

- 将下载的 ZIP 文件解压到一个文件夹，例如 `D:\hugo`
- 你应该能在`bin`文件夹中看到一个 `hugo.exe` 文件

## (3)配置环境变量

- **打开系统环境变量设置：**
  - 在搜索栏中输入 **“环境变量”**，选择 **“编辑系统环境变量”**
  - 点击 **“环境变量”** 按钮
- **添加 Hugo 到 PATH：**
  - 在 **系统变量** 下找到 `Path`，选中后点击 **编辑**
  - 点击 **新建**，输入 Hugo 的路径，例如：`D:\hugo\bin`
  - 点击 **确定**，保存所有设置

## (4)验证安装

- 打开命令提示符（`cmd`），输入以下命令：

```shell
hugo version
```

- 如果安装成功，你会看到类似下面的输出：

```
hugo v0.128.2-de36c1a95d28595d8243fd8b891665b069ed0850+extended windows/amd64 BuildDate=2024-07-04T08:13:25Z VendorInfo=gohugoio
```

## (5)初始化站点

- 创建新项目

```shell
hugo new site ryluiiwan.com
```

- 进入项目目录

```shell
cd ryluiiwan.com
```

## (6)初始化 git 仓库

- 初始化一个新的 git 仓库

```shell
git init
```

- 将**工作区中所有的更改**添加到暂存区（Staging Area）。它的作用是准备这些更改以便后续使用 `git commit` 提交到本地仓库

```shell
git add -A
```

- 提交你在暂存区中的更改到本地仓库，并为这个提交添加一条描述信息

```shell
git commit -m "first commit"
```

- **重命名当前分支**为 `main`,

```shell
git branch -M main
```

- 将远程仓库关联到本地仓库

```shell
git remote add origin git@github.com:ryluiiwan/ryluiiwan.com.git
```
