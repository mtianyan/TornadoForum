/**
 * Created by Think on 2018/8/11.
 */

new Vue({
    el: "#questions",

    created() {
        this.showname();
        this.getquestions("全部")
    },

    data() {
        return {
            res: [],
            type: 0,
            hotnumber: true
        }
    },
    computed: {
        user() {
            return store.state.username
        },
        notLogin() {
            return store.state.notLogin
        }
    },

    methods: {
        getquestions(category) {
            if (category == "全部") {
                this.type = 0
            } else if (category == "技术回答") {
                this.type = 1
            } else if (category == "技术分享") {
                this.type = 2
            }
            console.log(store.state.notLogin);
            let that = this;
            that.category = category;
            axios.get("http://127.0.0.1:8888/questions/", {
                params: {
                    "o": "new",
                    "c": category
                }
            })
                .then(function (response) {
                    that.res = response.data
                })
                .catch(function (err) {
                    console.log(err);
                });

        },
        questionOrder(order){
            let that = this;
            axios.get('/questions/?o='+order+"&c="+that.category,{
            }).then(function (req) {
                that.res = req.data;
            }).catch(function (err) {
                console.log(err)
            });
            if(order == 'new'){
                that.hotnumber = true
            }else {
                that.hotnumber = false
            }
        },
        showname() {
            return store.commit('showname')
        }

    }
})




