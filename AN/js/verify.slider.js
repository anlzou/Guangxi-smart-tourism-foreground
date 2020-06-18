/**
 * Notes: js滑动块验证码封装方法
 * User: ZHL
 * Date: 2020/5/14
 */
var verifyFun = {
	bar: function (item) {
		let html = '<div class="verify_box noselect"><div class="verify_forward_box"></div><div class="verify_drag_box" > > </div><div class="verify_tip">向右滑动></div></div>';
		item.dom.innerHTML = html;
		var verifyBox = item.dom.children[0];					// 滑道DOM
		var verifyLayer = item.dom.children[0].children[0];		// 遮罩层DOM
		var verifyDom = item.dom.children[0].children[1];		// 滑动块DOM
		var verifyTip = item.dom.children[0].children[2];		// 提示信息DOM
		verifyBox.style.width = parseInt(item.width) + 'px'; 		// 盒子宽
		verifyBox.style.height = parseInt(item.height) + 'px';	// 盒子高
		verifyDom.style.lineHeight = parseInt(item.height) + 'px';// 行高
		verifyDom.style.fontSize = parseInt(item.size) + 'px';	// 滑动块字体大小
		verifyDom.style.width = parseInt(item.height) + 'px';		// 滑块宽等于高
		verifyTip.style.fontSize = parseInt(item.hsize) + 'px';	// 提示文字大小
		verifyTip.style.lineHeight = parseInt(item.height) + 'px';// 提示文字行高
		var slideNum = parseInt(item.width) - parseInt(item.height); 	// 最大滑动距离
		var x = 0;
		var y = 0;
		var l = 0;
		var t = 0;
		var flag = false; // 开关
		/** PC-鼠标按下事件 **/
		verifyDom.onmousedown = function (e) {
			onstart(e);
		}
		/** PC-鼠标移动事件 **/
		verifyDom.onmousemove = function (e) {
			oncarry(e);
		}
		/** PC-鼠标抬起事件 **/
		verifyDom.onmouseup = function (e) {
			onend(e);
		}

		/** M-手指放到屏幕上时 **/
		verifyDom.ontouchstart = function (e) {
			onstart(e);
		}

		/** M-手指在屏幕上滑动时 **/
		verifyDom.ontouchmove = function (e) {
			oncarry(e);
		}

		/** M-手指离开屏幕时 **/
		verifyDom.ontouchend = function (e) {
			onend(e);
		}
		/** 鼠标移除事件 **/
		verifyDom.onmouseout = function (e) {
			flag = false;
			var ll = verifyDom.offsetLeft;
			if (ll < (slideNum - item.diff)) {
				verifyDom.style.left = l + 'px';
				verifyDom.style.top = t + 'px';
				verifyLayer.style.zIndex = 1;
			}
		}

		/** 一、鼠标按下事件/移动端手指放到屏幕上时触发方法 **/
		function onstart(e) {
			//获取x坐标和y坐标
			x = typeof (e.clientX) !== "undefined" ? e.clientX : e.changedTouches[0].clientX;
			y = typeof (e.clientY) !== "undefined" ? e.clientY : e.changedTouches[0].clientY;
			//获取左部和顶部的偏移量
			l = verifyDom.offsetLeft;
			t = verifyDom.offsetTop;
			flag = true;
		}
		/** 二、鼠标移动事件/移动端手指放到屏幕上时触发方法 **/
		function oncarry(e) {
			if (flag == false) {
				return;
			}
			//获取移动时x坐标和y坐标
			var nx = typeof (e.clientX) !== "undefined" ? e.clientX : e.changedTouches[0].clientX;
			var ny = typeof (e.clientY) !== "undefined" ? e.clientY : e.changedTouches[0].clientY;
			ny = y; // 水平滑动不让上下滑动，所以y始终一致
			nx = nx < x ? x : nx; // 控制最小 
			nx = nx - slideNum > x ? slideNum + x : nx; // 控制最大 
			//计算移动后的左偏移量和顶部的偏移量
			var nl = nx - (x - l);
			var nt = ny - (y - t);
			verifyDom.style.left = nl + 'px';
			verifyDom.style.top = nt + 'px';
			if (nl > (slideNum - item.diff)) {
				verifyDom.style.left = slideNum + 'px';
				verifyDom.style.top = t + 'px';
				verifyLayer.style.zIndex = 5;
				verifyDom.innerHTML = '&radic;';
				verifyDom.style.color = '#0a6af9';
				item.dom.children[0].style.border = '1px solid #0a6af9';
				verifyTip.innerText = '验证通过';
				verifyBox.style.background = '#fff';
				item.success();
			}
		}
		/** 三、鼠标抬起事件/手指离开屏幕时触发方法 **/
		function onend(e) {
			flag = false;
			var ll = verifyDom.offsetLeft;
			if (ll < (slideNum - item.diff)) {
				verifyDom.style.left = l + 'px';
				verifyDom.style.top = t + 'px';
				item.error();
			} else {
				verifyDom.style.left = slideNum + 'px';
				verifyDom.style.top = t + 'px';
				verifyLayer.style.zIndex = 5;
				verifyDom.innerHTML = '&radic;';
				verifyDom.style.color = '#0a6af9';
				item.dom.children[0].style.border = '1px solid #0a6af9';
				verifyTip.innerText = '验证通过';
				verifyBox.style.background = '#fff';
				item.success();
			}
		}

	},
	bar2: function () {
		// 其他
	}
};

/**
 * Notes: 验证码登录滑动条
 * User: anlzou
 * Date: 2020/6/18
 */
var type1 = document.getElementById('verify_type1');
verifyFun.bar({
	dom: type1,		// dom对象
	width: '318',	// 盒子宽
	height: '40',	// 盒子高
	hsize: '16',		// 提示字体大小
	size: '20',		// 滑动块箭头字体大小
	diff: 1,			// 误差值
	success: function () {
		alert('验证成功');
		//其他业务逻辑
	},
	error: function () {
		alert('验证失败！');
		//其他业务逻辑
	}
});
/**
 * Notes: 验证码注册滑动条
 * User: anlzou
 * Date: 2020/6/18
 */
var type1 = document.getElementById('verify_type2');
verifyFun.bar({
	dom: type1,		// dom对象
	width: '240',	// 盒子宽
	height: '40',	// 盒子高
	hsize: '16',		// 提示字体大小
	size: '20',		// 滑动块箭头字体大小
	diff: 1,			// 误差值
	success: function () {
		alert('验证成功');
		//其他业务逻辑
	},
	error: function () {
		alert('验证失败！');
		//其他业务逻辑
	}
});