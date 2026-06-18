# Week 5 TypeScript 学习环境

这个目录用于第 5 周 Day 1 和 Day 2 的 TypeScript 练习。Day 3 的 Next.js 项目按当天作业要求单独创建。

## 第一次使用

```bash
cd week-05
npm install
npm run check
npm run run:health
```

## 日常使用

把 `types-practice.ts`、`interface-practice.ts` 等练习文件放在本目录，然后运行：

```bash
npm run check
```

边写边检查：

```bash
npm run check:watch
```

运行一个 TypeScript 文件：

```bash
npx tsx 文件名.ts
```

不要全局安装依赖。项目会优先使用 `week-05/node_modules` 中锁定的版本。
