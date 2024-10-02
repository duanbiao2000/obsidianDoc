<template>
Editor
  
</template>
<script>
import EditorHeader from "../components/EditorHeader.vue";
import RichTextEditor from "../components/RichTextEditor.vue";
import request from "@/libb/utils";
import {imgDec} from "@/lib/config.js";

export default {
  components:
  {EditorHeader, RichTextEditor},
  data(){
    return{
      title:"",
      content:"",
      contentText:"",
      placeHolder:"",
      imgUrl: ""
    };
  },
  mounted(){
    if (parseFloat(this.$route.params.articleId)!==0){
      this.getArticle();
    }
  },
  methods:{
    uploadSuc(response){
      this.imgUrl=`${imgDec}${response.fileName}`;
    },
    updateContent(content, contentText){
      this.content=content;
      this.contentText=contentText;
    },
    releaseArticle(){
      if(parseFloat(this.$route.params.articleId)!==0){
        this.updateArticle();
      }else {
        this.createArticle();
      }
    },
    async createArticle(){
      await request
      .post("/articles",{
        content: this.content,
        excerpt: this.contentText.slice(0,100),
        title:this.title,
        imgUrl:this.imgUrl,
        userId:getCookies("id")
      })
      .then(res=>{
        if(res.code===201){
          this.$message.success("create success!");
          this.$router.push({
            path:`/article/$(res.data.id)`
          }); 
        } else {
          this.$message.error("res.error");
        }
      });
    },
    async getArticleInfo(){
      await request.get("/articles",{
        articleId:this.$route.params.articleId
      })
      .then(res=>{
        if(res.code===200){
          const articleInfo = res.data.content;
          this.content = articleInfo.content;
          this.imgUrl = articleInfo.cover;
          this.title = articleInfo.title;
          this.$refs.textEditor.updateContent(this.content);
        } else {
          this.$message.error("get article failure, try it again later");
          this.$router.go(-1);
        }
      });
    },
    async updateArticle(){
      await request.put("/articles",{
        articleId:this.$route.params.articleId,
        content: this.content,
        excerpt: this.contentText.slice(0,100),
        title:this.title,
        imgUrl:this.imgUrl,
        userId:getCookies("id")
      })
      .then(res=>{
        if(res.data.msg === [0]){
          this.$message.success("update failure, try it again later");
        } else{
          this.$message.success("update success!");
          this.$router.push({
            path:`/people/${getCookies("id")}/articles`
          });
        }
        });
      }
  }
}
</script>

<style></style>