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
    keyword:string[];
}

const mockSummary:SummaryResult ={
    summary:"Mock summary",
    mode:"brief",
    inputChars: 100,
    keyword:["sdasdad","dadad"]
}
//迁移挑战
