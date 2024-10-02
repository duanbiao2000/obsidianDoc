// 导入shallowMount函数和HelloWorld组件
import {shallowMount} from '@vue/test-utils';
import HelloWorld from '@/components/HelloWorld.vue';

// 测试HelloWorld组件
describe('HelloWorld.vue', () => {
  // 测试props.msg是否渲染正确
  it("renders props.msg when passed",()=>{
    // 定义props.msg的值
    const msg="new message";
    // 使用shallowMount函数挂载HelloWorld组件，并传入propsData
    const wrapper = shallowMount(HelloWorld,{propsData:{msg}});
  });
  // 断言wrapper的文本是否包含msg
  expect(wrapper.text()).toMatch(msg);
});