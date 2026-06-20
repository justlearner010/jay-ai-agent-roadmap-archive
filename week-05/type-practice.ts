type ReadingProgress = {
    bookTitle: string;
    pageRead: number;
    finished: boolean;
};

const msg:ReadingProgress ={
    bookTitle:"GEB",
    pageRead:100,
    finished: false

};

type SummaryMode = "brief" | "bullets";  /*这个|表示联合类型,只允许写规定里的字段*/


type SummaryResult = {
    summary: string;
    mode:SummaryMode;
    inputChars:number;
    keywords:string[];
}

const mockSummary:SummaryResult ={
    summary:"Mock summary",
    mode:"brief",
    inputChars: 100,
    keywords:["sdasdad","dadad"]
}
//迁移挑战

//2026-06-19跟做实验

interface UserProfile {
    name: string;
    level: number;
}


//核心动手任务
interface SummarizeRequest {
    text: string;
    mode: SummaryMode;
}

interface SummarizeResponse {
    summary: string;
    mode: SummaryMode;
    inputChars: number;
}

function validateUserProfile(
    value: unknown
): boolean {

    if (
        typeof value !== "object" ||
        value === null
    ) {
        return false;
    }

    // `as` 只告诉编译器按 UserProfile 读取，不会执行运行时校验。
    // 真正的校验由下面的 typeof 判断完成。
    const obj = value as UserProfile;

    if (typeof obj.name !== "string") {
        return false;
    }

    if (typeof obj.level !== "number") {
        return false;
    }

    return true;
}

function validateMockResponse(
    value: unknown
): boolean {

    if (
        typeof value !== "object" ||
        value === null
    ) {
        return false;
    }

    // 类型断言不会补字段或验证数据；下面的显式条件才是运行时校验。
    const obj = value as SummarizeResponse;

    if (typeof obj.summary !== "string") {
        return false;
    }

    if (
        obj.mode !== "brief" &&
        obj.mode !== "bullets"
    ) {
        return false;
    }

    if (
        typeof obj.inputChars !== "number"
    ) {
        return false;
    }

    return true;
}


const goodMock = {
    summary: "This is a summary.",
    mode: "brief",
    inputChars: 120
};

console.log(
    validateMockResponse(goodMock)
);

const missingInputChars = {
    summary: "This is a summary.",
    mode: "brief"
};

console.log(
    validateMockResponse(
        missingInputChars
    )
);

const wrongMode = {
    summary: "This is a summary.",
    mode: "short",
    inputChars: 120
};

console.log(
    validateMockResponse(
        wrongMode
    )
);
