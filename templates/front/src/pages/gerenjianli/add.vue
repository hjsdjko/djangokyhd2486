<template>
<div :style='{"width":"80%","padding":"20px","margin":"10px auto","position":"relative","background":"#fff"}'>
    <el-form
	  :style='{"width":"100%","position":"relative"}'
      class="add-update-preview"
      ref="ruleForm"
      :model="ruleForm"
      :rules="rules"
      label-width="100px"
    >
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="用户账号" prop="yonghuzhanghao">
            <el-input v-model="ruleForm.yonghuzhanghao" 
                placeholder="用户账号" clearable :disabled=" false  ||ro.yonghuzhanghao"></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="用户姓名" prop="yonghuxingming">
            <el-input v-model="ruleForm.yonghuxingming" 
                placeholder="用户姓名" clearable :disabled=" false  ||ro.yonghuxingming"></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="性别" prop="xingbie">
            <el-input v-model="ruleForm.xingbie" 
                placeholder="性别" clearable :disabled=" false  ||ro.xingbie"></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="手机" prop="shouji">
            <el-input v-model="ruleForm.shouji" 
                placeholder="手机" clearable :disabled=" false  ||ro.shouji"></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="头像" v-if="type!='cross' || (type=='cross' && !ro.touxiang)" prop="touxiang">
            <file-upload
            tip="点击上传头像"
            action="file/upload"
            :limit="3"
            :multiple="true"
            :fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
            @change="touxiangUploadChange"
            ></file-upload>
          </el-form-item>
            <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' class="upload" v-else label="头像" prop="touxiang">
                <img v-if="ruleForm.touxiang.substring(0,4)=='http'" class="upload-img" style="margin-right:20px;" v-bind:key="index" :src="ruleForm.touxiang.split(',')[0]" width="100" height="100">
                <img v-else class="upload-img" style="margin-right:20px;" v-bind:key="index" v-for="(item,index) in ruleForm.touxiang.split(',')" :src="baseUrl+item" width="100" height="100">
            </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="专业" prop="zhuanye">
            <el-input v-model="ruleForm.zhuanye" 
                placeholder="专业" clearable :disabled=" false  ||ro.zhuanye"></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="学历" prop="xueli">
            <el-input v-model="ruleForm.xueli" 
                placeholder="学历" clearable :disabled=" false  ||ro.xueli"></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="出生日期" prop="chushengriqi">
              <el-date-picker
				  :disabled=" false  ||ro.chushengriqi"
                  format="yyyy 年 MM 月 dd 日"
                  value-format="yyyy-MM-dd"
                  v-model="ruleForm.chushengriqi" 
                  type="date"
                  placeholder="出生日期">
              </el-date-picker> 
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="求职意向" prop="qiuzhiyixiang">
            <el-input v-model="ruleForm.qiuzhiyixiang" 
                placeholder="求职意向" clearable :disabled=" false  ||ro.qiuzhiyixiang"></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}'  label="意向职位" prop="yixiangzhiwei">
            <el-select v-model="ruleForm.yixiangzhiwei" placeholder="请选择意向职位" :disabled=" false  ||ro.yixiangzhiwei" >
              <el-option
                  v-for="(item,index) in yixiangzhiweiOptions"
                  :key="index"
                  :label="item"
                  :value="item">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="意向城市" prop="yixiangchengshi">
            <el-input v-model="ruleForm.yixiangchengshi" 
                placeholder="意向城市" clearable :disabled=" false  ||ro.yixiangchengshi"></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="薪资要求" prop="xinziyaoqiu">
            <el-input v-model="ruleForm.xinziyaoqiu" 
                placeholder="薪资要求" clearable :disabled=" false  ||ro.xinziyaoqiu"></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="教育背景" prop="jiaoyubeijing">
            <el-input v-model="ruleForm.jiaoyubeijing" 
                placeholder="教育背景" clearable :disabled=" false  ||ro.jiaoyubeijing"></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="获奖证书" prop="huojiangzhengshu">
            <el-input v-model="ruleForm.huojiangzhengshu" 
                placeholder="获奖证书" clearable :disabled=" false  ||ro.huojiangzhengshu"></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="简历文件" prop="jianliwenjian">
            <file-upload
            tip="点击上传简历文件"
            action="file/upload"
            :limit="1"
            :multiple="true"
            :fileUrls="ruleForm.jianliwenjian?ruleForm.jianliwenjian:''"
            @change="jianliwenjianUploadChange"
            ></file-upload>
          </el-form-item>  
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="工作经验" prop="gongzuojingyan">
            <el-input
              type="textarea"
              :rows="8"
              placeholder="工作经验"
              v-model="ruleForm.gongzuojingyan">
            </el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="项目经验" prop="xiangmujingyan">
            <el-input
              type="textarea"
              :rows="8"
              placeholder="项目经验"
              v-model="ruleForm.xiangmujingyan">
            </el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="个人技能" prop="gerenjineng">
            <el-input
              type="textarea"
              :rows="8"
              placeholder="个人技能"
              v-model="ruleForm.gerenjineng">
            </el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px","background":"none"}' label="自我评价" prop="ziwopingjia">
            <el-input
              type="textarea"
              :rows="8"
              placeholder="自我评价"
              v-model="ruleForm.ziwopingjia">
            </el-input>
          </el-form-item>

      <el-form-item :style='{"padding":"0","margin":"0"}'>
        <el-button :style='{"border":"0","cursor":"pointer","padding":"0","margin":"0 20px 0 0","outline":"none","color":"rgba(255, 255, 255, 1)","borderRadius":"5px","background":"#57A7A5","width":"128px","lineHeight":"40px","fontSize":"16px","height":"40px"}'  type="primary" @click="onSubmit">提交</el-button>
        <el-button :style='{"border":"none","cursor":"pointer","padding":"0","margin":"0","outline":"none","color":"rgba(64, 158, 255, 1)","borderRadius":"5px","background":"#9E9E9E","width":"128px","lineHeight":"40px","fontSize":"16px","height":"40px"}' @click="back()">返回</el-button>
      </el-form-item>
    </el-form>
</div>
</template>

<script>
  export default {
    data() {
	  let self = this
      return {
        id: '',
        baseUrl: '',
        ro:{
				yonghuzhanghao : false,
				yonghuxingming : false,
				xingbie : false,
				shouji : false,
				touxiang : false,
				zhuanye : false,
				xueli : false,
				chushengriqi : false,
				qiuzhiyixiang : false,
				yixiangzhiwei : false,
				yixiangchengshi : false,
				xinziyaoqiu : false,
				jiaoyubeijing : false,
				huojiangzhengshu : false,
				gongzuojingyan : false,
				xiangmujingyan : false,
				gerenjineng : false,
				ziwopingjia : false,
				jianliwenjian : false,
				storeupnum : false,
        },
        type: '',
        userTableName: localStorage.getItem('UserTableName'),
        ruleForm: {
          yonghuzhanghao: '',
          yonghuxingming: '',
          xingbie: '',
          shouji: '',
          touxiang: '',
          zhuanye: '',
          xueli: '',
          chushengriqi: '',
          qiuzhiyixiang: '',
          yixiangzhiwei: '',
          yixiangchengshi: '',
          xinziyaoqiu: '',
          jiaoyubeijing: '',
          huojiangzhengshu: '',
          gongzuojingyan: '',
          xiangmujingyan: '',
          gerenjineng: '',
          ziwopingjia: '',
          jianliwenjian: '',
          storeupnum: '',
        },
        yixiangzhiweiOptions: [],


        rules: {
          yonghuzhanghao: [
          ],
          yonghuxingming: [
          ],
          xingbie: [
          ],
          shouji: [
          ],
          touxiang: [
          ],
          zhuanye: [
          ],
          xueli: [
          ],
          chushengriqi: [
          ],
          qiuzhiyixiang: [
          ],
          yixiangzhiwei: [
          ],
          yixiangchengshi: [
          ],
          xinziyaoqiu: [
          ],
          jiaoyubeijing: [
          ],
          huojiangzhengshu: [
          ],
          gongzuojingyan: [
          ],
          xiangmujingyan: [
          ],
          gerenjineng: [
          ],
          ziwopingjia: [
          ],
          jianliwenjian: [
          ],
          storeupnum: [
            { validator: this.$validate.isIntNumer, trigger: 'blur' },
          ],
        },
		centerType: false,
      };
    },
    computed: {



    },
    components: {
    },
    created() {
		if(this.$route.query.centerType){
			this.centerType = true
		}
	  //this.bg();
      let type = this.$route.query.type ? this.$route.query.type : '';
      this.init(type);
      this.baseUrl = this.$config.baseUrl;
      this.ruleForm.chushengriqi = this.getCurDate()
    },
    methods: {
      getMakeZero(s) {
          return s < 10 ? '0' + s : s;
      },
      // 下载
      download(file){
        window.open(`${file}`)
      },
      // 初始化
      init(type) {
        this.type = type;
        if(type=='cross'){
          var obj = JSON.parse(localStorage.getItem('crossObj'));
          for (var o in obj){
            if(o=='yonghuzhanghao'){
              this.ruleForm.yonghuzhanghao = obj[o];
              this.ro.yonghuzhanghao = true;
              continue;
            }
            if(o=='yonghuxingming'){
              this.ruleForm.yonghuxingming = obj[o];
              this.ro.yonghuxingming = true;
              continue;
            }
            if(o=='xingbie'){
              this.ruleForm.xingbie = obj[o];
              this.ro.xingbie = true;
              continue;
            }
            if(o=='shouji'){
              this.ruleForm.shouji = obj[o];
              this.ro.shouji = true;
              continue;
            }
            if(o=='touxiang'){
              this.ruleForm.touxiang = obj[o].split(",")[0];
              this.ro.touxiang = true;
              continue;
            }
            if(o=='zhuanye'){
              this.ruleForm.zhuanye = obj[o];
              this.ro.zhuanye = true;
              continue;
            }
            if(o=='xueli'){
              this.ruleForm.xueli = obj[o];
              this.ro.xueli = true;
              continue;
            }
            if(o=='chushengriqi'){
              this.ruleForm.chushengriqi = obj[o];
              this.ro.chushengriqi = true;
              continue;
            }
            if(o=='qiuzhiyixiang'){
              this.ruleForm.qiuzhiyixiang = obj[o];
              this.ro.qiuzhiyixiang = true;
              continue;
            }
            if(o=='yixiangzhiwei'){
              this.ruleForm.yixiangzhiwei = obj[o];
              this.ro.yixiangzhiwei = true;
              continue;
            }
            if(o=='yixiangchengshi'){
              this.ruleForm.yixiangchengshi = obj[o];
              this.ro.yixiangchengshi = true;
              continue;
            }
            if(o=='xinziyaoqiu'){
              this.ruleForm.xinziyaoqiu = obj[o];
              this.ro.xinziyaoqiu = true;
              continue;
            }
            if(o=='jiaoyubeijing'){
              this.ruleForm.jiaoyubeijing = obj[o];
              this.ro.jiaoyubeijing = true;
              continue;
            }
            if(o=='huojiangzhengshu'){
              this.ruleForm.huojiangzhengshu = obj[o];
              this.ro.huojiangzhengshu = true;
              continue;
            }
            if(o=='gongzuojingyan'){
              this.ruleForm.gongzuojingyan = obj[o];
              this.ro.gongzuojingyan = true;
              continue;
            }
            if(o=='xiangmujingyan'){
              this.ruleForm.xiangmujingyan = obj[o];
              this.ro.xiangmujingyan = true;
              continue;
            }
            if(o=='gerenjineng'){
              this.ruleForm.gerenjineng = obj[o];
              this.ro.gerenjineng = true;
              continue;
            }
            if(o=='ziwopingjia'){
              this.ruleForm.ziwopingjia = obj[o];
              this.ro.ziwopingjia = true;
              continue;
            }
            if(o=='jianliwenjian'){
              this.ruleForm.jianliwenjian = obj[o];
              this.ro.jianliwenjian = true;
              continue;
            }
            if(o=='storeupnum'){
              this.ruleForm.storeupnum = obj[o];
              this.ro.storeupnum = true;
              continue;
            }
          }
        }else if(type=='edit'){
			this.info()
		}
        // 获取用户信息
        this.$http.get(this.userTableName + '/session', {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            var json = res.data.data;
            if((json.yonghuzhanghao!=''&&json.yonghuzhanghao) || json.yonghuzhanghao==0){
                this.ruleForm.yonghuzhanghao = json.yonghuzhanghao
            }
            if((json.yonghuxingming!=''&&json.yonghuxingming) || json.yonghuxingming==0){
                this.ruleForm.yonghuxingming = json.yonghuxingming
            }
            if((json.xingbie!=''&&json.xingbie) || json.xingbie==0){
                this.ruleForm.xingbie = json.xingbie
            }
            if((json.shouji!=''&&json.shouji) || json.shouji==0){
                this.ruleForm.shouji = json.shouji
            }
            if((json.touxiang!=''&&json.touxiang) || json.touxiang==0){
                this.ruleForm.touxiang = json.touxiang
            }
          }
        });
        this.$http.get('option/zhiweileixing/zhiweileixing', {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            this.yixiangzhiweiOptions = res.data.data;
          }
        });

		if (localStorage.getItem('raffleType') && localStorage.getItem('raffleType') != null) {
			localStorage.removeItem('raffleType')
			setTimeout(() => {
				this.onSubmit()
			}, 300)
		}
      },

    // 多级联动参数
      // 多级联动参数
      info() {
        this.$http.get(`gerenjianli/detail/${this.$route.query.id}`, {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            this.ruleForm = res.data.data;
          }
        });
      },
      // 提交
      onSubmit() {

			//更新跨表属性
			var crossuserid;
			var crossrefid;
			var crossoptnum;
			this.$refs["ruleForm"].validate(valid => {
				if(valid) {
					if(this.type=='cross'){
						var statusColumnName = localStorage.getItem('statusColumnName');
						var statusColumnValue = localStorage.getItem('statusColumnValue');
						if(statusColumnName && statusColumnName!='') {
							var obj = JSON.parse(localStorage.getItem('crossObj'));
							if(!statusColumnName.startsWith("[")) {
								for (var o in obj){
									if(o==statusColumnName){
										obj[o] = statusColumnValue;
									}
								}
								var table = localStorage.getItem('crossTable');
								this.$http.post(table+'/update', obj).then(res => {});
							} else {
								crossuserid=Number(localStorage.getItem('frontUserid'));
								crossrefid=obj['id'];
								crossoptnum=localStorage.getItem('statusColumnName');
								crossoptnum=crossoptnum.replace(/\[/,"").replace(/\]/,"");
							}
						}
					}
					if(crossrefid && crossuserid) {
						this.ruleForm.crossuserid=crossuserid;
						this.ruleForm.crossrefid=crossrefid;
						var params = {
							page: 1,
							limit: 10,
							crossuserid:crossuserid,
							crossrefid:crossrefid,
						}
						this.$http.get('gerenjianli/list', {
							params: params
						}).then(res => {
							if(res.data.data.total>=crossoptnum) {
								this.$message({
									message: localStorage.getItem('tips'),
									type: 'error',
									duration: 1500,
								});
								return false;
							} else {
								// 跨表计算


								this.$http.post(`gerenjianli/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(res => {
									if (res.data.code == 0) {
										this.$message({
											message: '操作成功',
											type: 'success',
											duration: 1500,
											onClose: () => {
												this.$router.go(-1);
											}
										});
									} else {
										this.$message({
											message: res.data.msg,
											type: 'error',
											duration: 1500
										});
									}
								});
							}
						});
					} else {


						this.$http.post(`gerenjianli/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(res => {
							if (res.data.code == 0) {
								this.$message({
									message: '操作成功',
									type: 'success',
									duration: 1500,
									onClose: () => {
										this.$router.go(-1);
									}
								});
							} else {
								this.$message({
									message: res.data.msg,
									type: 'error',
									duration: 1500
								});
							}
						});
					}
				}
			});
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
		// 返回
		back() {
			this.$router.go(-1);
		},
      touxiangUploadChange(fileUrls) {
          this.ruleForm.touxiang = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");;
      },
      jianliwenjianUploadChange(fileUrls) {
          this.ruleForm.jianliwenjian = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");;
      },
    }
  };
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.el-date-editor.el-input {
		width: auto;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
	  padding: 0 10px 0 0;
	  color: #000;
	  font-weight: 500;
	  width: 100px;
	  font-size: 14px;
	  line-height: 40px;
	  text-align: right;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
	  margin-left: 100px;
	}
	
	.add-update-preview .el-input /deep/ .el-input__inner {
	  border: 1px solid #E2E3E5;
	  border-radius: 0;
	  padding: 0 12px;
	  box-shadow: none;
	  outline: none;
	  color: #000;
	  width: 500px;
	  font-size: 14px;
	  height: 40px;
	}
	.add-update-preview .el-input-number /deep/ .el-input__inner {
		text-align: left;
	  border: 1px solid #E2E3E5;
	  border-radius: 0;
	  padding: 0 12px;
	  box-shadow: none;
	  outline: none;
	  color: #000;
	  width: 500px;
	  font-size: 14px;
	  height: 40px;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__decrease {
		display: none;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__increase {
		display: none;
	}
	
	.add-update-preview .el-select /deep/ .el-input__inner {
	  border: 1px solid #E2E3E5;
	  border-radius: 0;
	  padding: 0 10px;
	  box-shadow: none;
	  outline: none;
	  color: #000;
	  width: 500px;
	  font-size: 14px;
	  height: 40px;
	}
	
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
	  border: 1px solid #E2E3E5;
	  border-radius: 0;
	  padding: 0 10px 0 30px;
	  box-shadow: none;
	  outline: none;
	  color: none;
	  width: 500px;
	  font-size: 14px;
	  height: 40px;
	}
	
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .upload .upload-img {
	  border: 1px solid #E2E3E5;
	  cursor: pointer;
	  border-radius: 0;
	  color: #000;
	  width: 200px;
	  font-size: 32px;
	  line-height: 60px;
	  text-align: center;
	  height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
	  border: 1px solid #E2E3E5;
	  cursor: pointer;
	  border-radius: 0;
	  color: #000;
	  width: 200px;
	  font-size: 32px;
	  line-height: 60px;
	  text-align: center;
	  height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
	  border: 1px solid #E2E3E5;
	  cursor: pointer;
	  border-radius: 0;
	  color: #000;
	  width: 200px;
	  font-size: 32px;
	  line-height: 60px;
	  text-align: center;
	  height: 60px;
	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
	  border: 1px solid #E2E3E5;
	  border-radius: 0;
	  padding: 12px;
	  box-shadow: none;
	  outline: none;
	  color: #000;
	  width: 500px;
	  font-size: 14px;
	  height: 120px;
	}
</style>
